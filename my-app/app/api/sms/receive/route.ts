import { NextRequest, NextResponse } from "next/server";

/**
 * GET/POST /api/sms/receive
 *
 * Vonage Inbound SMS Webhook.
 * Configure this URL in your Vonage Dashboard under:
 *   Settings → SMS → Inbound webhook URL
 *
 * Vonage sends either GET or POST (depending on your dashboard setting).
 * This handler accepts both.
 *
 * Payload fields from Vonage:
 *   msisdn   – sender's phone number (E.164 without +)
 *   to       – your Vonage virtual number
 *   text     – message body
 *   type     – "text" | "unicode" | "binary"
 *   messageId, timestamp, etc.
 */

async function handleInbound(params: Record<string, string>) {
  const { msisdn, to, text, type, messageId } = params;

  console.log("[/api/sms/receive] Inbound SMS:", {
    from: msisdn,
    to,
    text,
    type,
    messageId,
  });

  // ── Command routing ───────────────────────────────────────────────────────
  // Parse the text as a command (e.g., user texts "STATUS" or "HELP")
  const command = text?.trim().toUpperCase();

  switch (command) {
    case "HELP":
      console.log(`[SMS Command] HELP requested from ${msisdn}`);
      // TODO: auto-reply with help text via /api/sms/send
      break;

    case "STATUS":
      console.log(`[SMS Command] STATUS requested from ${msisdn}`);
      // TODO: look up user status and reply
      break;

    case "STOP":
      console.log(`[SMS Command] STOP (opt-out) from ${msisdn}`);
      // TODO: mark number as opted-out in Supabase
      break;

    default:
      console.log(`[SMS Command] Unrecognized command "${text}" from ${msisdn}`);
      break;
  }

  // ── Persist to Supabase (optional, wire in later) ─────────────────────────
  // const supabase = createServiceClient();
  // await supabase.from("sms_inbox").insert({ from: msisdn, to, text, message_id: messageId });
}

export async function GET(req: NextRequest) {
  const params = Object.fromEntries(req.nextUrl.searchParams.entries());
  await handleInbound(params as Record<string, string>);
  return new NextResponse("OK", { status: 200 });
}

export async function POST(req: NextRequest) {
  let params: Record<string, string> = {};
  const contentType = req.headers.get("content-type") ?? "";

  if (contentType.includes("application/json")) {
    params = await req.json();
  } else {
    // application/x-www-form-urlencoded (Vonage default)
    const text = await req.text();
    params = Object.fromEntries(new URLSearchParams(text).entries());
  }

  await handleInbound(params);
  return new NextResponse("OK", { status: 200 });
}
