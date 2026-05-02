"use client";

import { useAuthStore } from "@/store/authStore";
import { useEffect } from "react";

export default function DashboardPage() {
  const { user, fetchCurrentUser } = useAuthStore();

  useEffect(() => {
    fetchCurrentUser();
  }, []);

  return (
    <div>
      <h1 className="text-4xl font-bold mb-8">Bem-vindo, {user?.first_name}!</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="card">
          <h3 className="text-lg font-semibold mb-2">Meus Agendamentos</h3>
          <p className="text-3xl font-bold text-primary">0</p>
          <p className="text-gray-600 text-sm mt-2">Serviços agendados</p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold mb-2">Avaliação</h3>
          <p className="text-3xl font-bold text-warning">5.0</p>
          <p className="text-gray-600 text-sm mt-2">Sua avaliação média</p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold mb-2">Perfil</h3>
          <p className="text-gray-600">{user?.role === 'technician' ? 'Técnico' : 'Cliente'}</p>
          <p className="text-gray-600 text-sm mt-2">Tipo de conta</p>
        </div>
      </div>
    </div>
  );
}
