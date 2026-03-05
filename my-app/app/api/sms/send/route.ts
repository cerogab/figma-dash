import { NextRequest, NextResponse } from "next/server";
import { vonage, VONAGE_FROM } from "@/lib/vonage";
import { createClient } from "@/lib/supabase/server";

/**
 * POST /api/sms/send
 *
 * Body: { to: string, text: string }
 *
 * Protected — user must be authenticated via Supabase session.
 * Sends an SMS via Vonage and returns the message ID.
 */
export async function POST(req: NextRequest) {
  // ── Auth guard ────────────────────────────────────────────────────────────
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  // ── Parse body ────────────────────────────────────────────────────────────
  let to: string, text: string;
  try {
    ({ to, text } = await req.json());
  } catch {
    return NextResponse.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  if (!to || !text) {
    return NextResponse.json(
      { error: "Missing required fields: to, text" },
      { status: 400 }
    );
  }

  // Strip non-digit chars and ensure E.164 format (+1XXXXXXXXXX)
  const cleaned = to.replace(/\D/g, "");
  if (cleaned.length < 10) {
    return NextResponse.json(
      { error: "Invalid phone number. Use E.164 format e.g. +12025551234" },
      { status: 400 }
    );
  }

  // ── Send SMS ──────────────────────────────────────────────────────────────
  try {
    const response = await vonage.sms.send({
      to: cleaned,
      from: VONAGE_FROM,
      text,
    });

    const msg = response.messages[0];

    if (msg.status !== "0") {
      return NextResponse.json(
        { error: `Vonage error: ${msg["error-text"]}` },
        { status: 502 }
      );
    }

    return NextResponse.json({
      success: true,
      messageId: msg["message-id"],
      to: msg.to,
      remainingBalance: msg["remaining-balance"],
    });
  } catch (err: unknown) {
    console.error("[/api/sms/send] Error:", err);
    return NextResponse.json(
      { error: "Failed to send SMS" },
      { status: 500 }
    );
  }
}
