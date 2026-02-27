import Script from "next/script";
import type { Metadata } from "next";
import { Geist } from "next/font/google";
import { ThemeProvider } from "next-themes";
import "./globals.css";

const defaultUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : "http://localhost:3000";

export const metadata: Metadata = {
  metadataBase: new URL(defaultUrl),
  title: "Next.js and Supabase Starter Kit",
  description: "The fastest way to build apps with Next.js and Supabase",
};

const geistSans = Geist({
  variable: "--font-geist-sans",
  display: "swap",
  subsets: ["latin"],
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${geistSans.className} antialiased`}>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
        <Script
          id="iubenda-loader"
          strategy="lazyOnload"
          dangerouslySetInnerHTML={{
            __html: `
              (function (w, d) {
                var loader = function () {
                  var s = d.createElement("script"),
                    tag = d.getElementsByTagName("script")[0];
                  s.src = "https://cdn.iubenda.com/iubenda.js";
                  tag.parentNode.insertBefore(s, tag);
                };
                if (w.addEventListener) {
                  w.addEventListener("load", loader, false);
                } else if (w.attachEvent) {
                  w.attachEvent("onload", loader);
                } else {
                  w.onload = loader;
                }
              })(window, document);
            `,
          }}
        />
      </body>
    </html>
  );
}
