import { Vonage } from "@vonage/server-sdk";

// Vonage client — initialized once and reused across API routes
if (!process.env.VONAGE_API_KEY || !process.env.VONAGE_API_SECRET) {
  throw new Error(
    "Missing Vonage credentials. Set VONAGE_API_KEY and VONAGE_API_SECRET in .env.local"
  );
}

export const vonage = new Vonage({
  apiKey: process.env.VONAGE_API_KEY!,
  apiSecret: process.env.VONAGE_API_SECRET!,
});

/** The Vonage virtual number messages are sent FROM */
export const VONAGE_FROM = process.env.VONAGE_FROM_NUMBER ?? "Vonage";
