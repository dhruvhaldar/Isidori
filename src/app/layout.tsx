import "./globals.css";
import type { Metadata } from "next";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export const metadata: Metadata = {
  title: "Isidori - Geometric Control Theory",
  description: "Educational tool for geometric control theory based on SF2842.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-background font-sans antialiased flex flex-col">
        <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
          <div className="container flex h-14 items-center">
            <div className="mr-4 hidden md:flex">
              <Link className="mr-6 flex items-center space-x-2" href="/">
                <span className="hidden font-bold sm:inline-block">Isidori</span>
              </Link>
              <nav className="flex items-center space-x-6 text-sm font-medium">
                <Link className="transition-colors hover:text-foreground/80 text-foreground/60" href="/linear">Linear Systems</Link>
                <Link className="transition-colors hover:text-foreground/80 text-foreground/60" href="/nonlinear">Nonlinear Systems</Link>
                <Link className="transition-colors hover:text-foreground/80 text-foreground/60" href="/simulate">Simulation</Link>
              </nav>
            </div>
          </div>
        </header>
        <main className="flex-1 container py-6">
          {children}
        </main>
        <footer className="py-6 md:px-8 md:py-0">
          <div className="container flex flex-col items-center justify-between gap-4 md:h-24 md:flex-row">
            <p className="text-balance text-center text-sm leading-loose text-muted-foreground md:text-left">
              Built for KTH Course SF2842. MIT License.
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
}
