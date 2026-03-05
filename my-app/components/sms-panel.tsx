"use client";

import { useState } from "react";

type SendResult = {
  success?: boolean;
  messageId?: string;
  to?: string;
  remainingBalance?: string;
  error?: string;
};

export function SmsPanel() {
  const [to, setTo] = useState("");
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<SendResult | null>(null);

  async function handleSend(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch("/api/sms/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ to, text }),
      });

      const data: SendResult = await res.json();
      setResult(data);

      if (data.success) {
        setText(""); // clear message on success, keep the number
      }
    } catch {
      setResult({ error: "Network error — could not reach the API." });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col gap-6 max-w-lg w-full">
      {/* ── Send Form ── */}
      <form
        onSubmit={handleSend}
        className="flex flex-col gap-4 border rounded-lg p-6 bg-card"
      >
        <h3 className="font-semibold text-lg">Send SMS</h3>

        {/* To */}
        <div className="flex flex-col gap-1">
          <label
            htmlFor="sms-to"
            className="text-sm font-medium text-foreground"
          >
            To (E.164 format)
          </label>
          <input
            id="sms-to"
            type="tel"
            placeholder="+12025551234"
            value={to}
            onChange={(e) => setTo(e.target.value)}
            required
            className="border rounded-md px-3 py-2 text-sm bg-background focus:outline-none focus:ring-2 focus:ring-ring"
          />
        </div>

        {/* Message */}
        <div className="flex flex-col gap-1">
          <label
            htmlFor="sms-text"
            className="text-sm font-medium text-foreground"
          >
            Message
          </label>
          <textarea
            id="sms-text"
            placeholder="Type your message…"
            value={text}
            onChange={(e) => setText(e.target.value)}
            required
            rows={4}
            maxLength={160}
            className="border rounded-md px-3 py-2 text-sm bg-background focus:outline-none focus:ring-2 focus:ring-ring resize-none"
          />
          <p className="text-xs text-muted-foreground text-right">
            {text.length}/160
          </p>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="bg-primary text-primary-foreground rounded-md px-4 py-2 text-sm font-medium hover:bg-primary/90 disabled:opacity-50 transition-colors"
        >
          {loading ? "Sending…" : "Send SMS"}
        </button>
      </form>

      {/* ── Result ── */}
      {result && (
        <div
          className={`rounded-md p-4 text-sm ${
            result.success
              ? "bg-green-50 border border-green-200 text-green-800 dark:bg-green-900/20 dark:border-green-800 dark:text-green-300"
              : "bg-red-50 border border-red-200 text-red-800 dark:bg-red-900/20 dark:border-red-800 dark:text-red-300"
          }`}
        >
          {result.success ? (
            <div className="flex flex-col gap-1">
              <p className="font-semibold">✓ Message sent!</p>
              <p>Message ID: <code className="font-mono">{result.messageId}</code></p>
              <p>Sent to: <code className="font-mono">{result.to}</code></p>
              {result.remainingBalance && (
                <p>Balance remaining: {result.remainingBalance}</p>
              )}
            </div>
          ) : (
            <p>✗ Error: {result.error}</p>
          )}
        </div>
      )}

      {/* ── Webhook Info ── */}
      <div className="border rounded-lg p-4 bg-muted/40 text-sm flex flex-col gap-2">
        <p className="font-semibold text-foreground">Vonage Webhook URLs</p>
        <p className="text-muted-foreground text-xs">
          Register these in your{" "}
          <a
            href="https://dashboard.nexmo.com/settings"
            target="_blank"
            rel="noreferrer"
            className="underline"
          >
            Vonage Dashboard → Settings
          </a>
          :
        </p>
        <div className="flex flex-col gap-1 font-mono text-xs bg-background rounded p-2 border">
          <p>
            <span className="text-muted-foreground">Inbound SMS: </span>
            <span>/api/sms/receive</span>
          </p>
          <p>
            <span className="text-muted-foreground">Delivery Status: </span>
            <span>/api/sms/status</span>
          </p>
        </div>
      </div>
    </div>
  );
}
