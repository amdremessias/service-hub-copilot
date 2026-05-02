import type { Metadata } from "next";
import "@/styles/globals.css";

export const metadata: Metadata = {
  title: "Service Hub - Marketplace de Técnicos",
  description: "Conectando clientes a técnicos qualificados",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <body>
        <div className="min-h-screen bg-light">
          {children}
        </div>
      </body>
    </html>
  );
}
