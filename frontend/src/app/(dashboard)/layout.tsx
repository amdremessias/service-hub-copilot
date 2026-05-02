"use client";

import { useAuthStore } from "@/store/authStore";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import Link from "next/link";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter();
  const { user, isAuthenticated, logout, fetchCurrentUser } = useAuthStore();

  useEffect(() => {
    if (!isAuthenticated) {
      fetchCurrentUser();
    }
  }, []);

  const handleLogout = () => {
    logout();
    router.push("/");
  };

  if (!isAuthenticated) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-gray-600">Carregando...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-light">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-primary">
            Service Hub
          </Link>
          <nav className="flex space-x-6 items-center">
            <Link href="/dashboard" className="text-dark hover:text-primary">
              Dashboard
            </Link>
            <Link href="/services" className="text-dark hover:text-primary">
              Serviços
            </Link>
            <Link href="/bookings" className="text-dark hover:text-primary">
              Meus Agendamentos
            </Link>
            <Link href="/profile" className="text-dark hover:text-primary">
              Perfil
            </Link>
            <button
              onClick={handleLogout}
              className="btn-outline text-sm"
            >
              Sair
            </button>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        {children}
      </main>
    </div>
  );
}
