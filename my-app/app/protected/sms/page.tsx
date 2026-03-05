import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { SmsPanel } from "@/components/sms-panel";
import { MessageSquare } from "lucide-react";

export default async function SmsPage() {
  // Auth guard — redirect to login if not signed in
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    redirect("/auth/login");
  }

  return (
    <div className="flex-1 w-full flex flex-col gap-8">
      {/* Header */}
      <div className="flex items-center gap-3">
        <MessageSquare size={28} strokeWidth={1.5} />
        <div>
          <h1 className="text-2xl font-bold">SMS Dashboard</h1>
          <p className="text-sm text-muted-foreground">
            Send messages and manage Vonage SMS settings
          </p>
        </div>
      </div>

      {/* API Pathway overview */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-sm">
        <div className="border rounded-lg p-4 bg-card flex flex-col gap-1">
          <p className="font-semibold text-foreground">📤 Send SMS</p>
          <code className="text-xs font-mono text-muted-foreground">
            POST /api/sms/send
          </code>
          <p className="text-xs text-muted-foreground mt-1">
            Authenticated. Sends a message via Vonage.
          </p>
        </div>
        <div className="border rounded-lg p-4 bg-card flex flex-col gap-1">
          <p className="font-semibold text-foreground">📥 Receive SMS</p>
          <code className="text-xs font-mono text-muted-foreground">
            GET|POST /api/sms/receive
          </code>
          <p className="text-xs text-muted-foreground mt-1">
            Vonage inbound webhook. Handles commands (HELP, STATUS, STOP).
          </p>
        </div>
        <div className="border rounded-lg p-4 bg-card flex flex-col gap-1">
          <p className="font-semibold text-foreground">📋 Delivery Status</p>
          <code className="text-xs font-mono text-muted-foreground">
            GET|POST /api/sms/status
          </code>
          <p className="text-xs text-muted-foreground mt-1">
            Vonage DLR webhook. Tracks delivered, failed, expired statuses.
          </p>
        </div>
      </div>

      {/* SMS Send Panel */}
      <SmsPanel />
    </div>
  );
}
