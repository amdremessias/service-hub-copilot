"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/store/authStore";
import toast from "react-hot-toast";

export default function LoginPage() {
  const router = useRouter();
  const { login, isLoading, error } = useAuthStore();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(email, password);
      toast.success("Login realizado com sucesso!");
      router.push("/dashboard");
    } catch (err) {
      toast.error(error || "Erro ao fazer login");
    }
  };

  return (
    <div>
      <h1 className="text-3xl font-bold text-center mb-2">Service Hub</h1>
      <p className="text-gray-600 text-center mb-8">Conectando técnicos e clientes</p>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-dark mb-1">
            Email
          </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="input-field"
            placeholder="seu@email.com"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-dark mb-1">
            Senha
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="input-field"
            placeholder="Sua senha"
            required
          />
        </div>

        {error && <div className="text-danger text-sm">{error}</div>}

        <button
          type="submit"
          disabled={isLoading}
          className="btn-primary w-full"
        >
          {isLoading ? "Entrando..." : "Entrar"}
        </button>
      </form>

      <p className="text-center text-gray-600 text-sm mt-6">
        Não tem conta?{" "}
        <Link href="/auth/register" className="text-primary font-medium hover:underline">
          Registre-se
        </Link>
      </p>
    </div>
  );
}
