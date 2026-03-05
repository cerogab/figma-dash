import { NextRequest, NextResponse } from "next/server";

/**
 * GET/POST /api/sms/status
 *
 * Vonage Delivery Receipt (DLR) Webhook.
 * Configure this URL in your Vonage Dashboard under:
 *   Settings → SMS → Status webhook URL
 *
 * Vonage sends delivery status updates for every outbound message.
 *
 * Status values:
 *   delivered   – message delivered to handset
 *   failed      – delivery failed
 *   rejected    – rejected by carrier
 *   accepted    – accepted by carrier, awaiting delivery
 *   buffered    – message buffered (e.g., handset off)
 *   expired     – TTL exceeded
 *   unknown     – unknown status
 */

type DeliveryReceipt = {
  messageId?: string;
  "message-id"?: string;
  msisdn?: string;
  to?: string;
  status?: string;
  "err-code"?: string;
  timestamp?: string;
  price?: string;
  scts?: string;
};

async function handleStatus(params: DeliveryReceipt) {
  const messageId = params.messageId ?? params["message-id"];
  const { msisdn, to, status } = params;
  const errCode = params["err-code"];

  console.log("[/api/sms/status] Delivery receipt:", {
    messageId,
    to: msisdn,
    from: to,
    status,
    errCode,
  });

  // ── Handle specific statuses ──────────────────────────────────────────────
  switch (status) {
    case "delivered":
      console.log(`[DLR] Message ${messageId} delivered to ${msisdn}`);
      // TODO: update delivery status in Supabase
      break;

    case "failed":
    case "rejected":
      console.warn(`[DLR] Message ${messageId} FAILED. Error code: ${errCode}`);
      // TODO: flag failed delivery in Supabase / trigger retry logic
      break;

    case "accepted":
    case "buffered":
      console.log(`[DLR] Message ${messageId} status: ${status}`);
      break;

    case "expired":
      console.warn(`[DLR] Message ${messageId} expired before delivery`);
      break;

    default:
      console.log(`[DLR] Message ${messageId} unknown status: ${status}`);
  }
}

export async function GET(req: NextRequest) {
  const params = Object.fromEntries(req.nextUrl.searchParams.entries());
  await handleStatus(params as DeliveryReceipt);
  return new NextResponse("OK", { status: 200 });
}

export async function POST(req: NextRequest) {
  let params: DeliveryReceipt = {};
  const contentType = req.headers.get("content-type") ?? "";

  if (contentType.includes("application/json")) {
    params = await req.json();
  } else {
    const text = await req.text();
    params = Object.fromEntries(
      new URLSearchParams(text).entries()
    ) as DeliveryReceipt;
  }

  await handleStatus(params);
  return new NextResponse("OK", { status: 200 });
}
