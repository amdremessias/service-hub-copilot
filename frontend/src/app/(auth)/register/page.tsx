"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/store/authStore";
import toast from "react-hot-toast";

export default function RegisterPage() {
  const router = useRouter();
  const { register, isLoading, error } = useAuthStore();
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    firstName: "",
    lastName: "",
    role: "client",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      toast.error("As senhas não correspondem");
      return;
    }

    try {
      await register(
        formData.email,
        formData.password,
        formData.firstName,
        formData.lastName,
        formData.role
      );
      toast.success("Registro realizado com sucesso!");
      router.push("/dashboard");
    } catch (err) {
      toast.error(error || "Erro ao registrar");
    }
  };

  return (
    <div>
      <h1 className="text-3xl font-bold text-center mb-2">Criar Conta</h1>
      <p className="text-gray-600 text-center mb-8">Junte-se ao Service Hub</p>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-dark mb-1">
              Nome
            </label>
            <input
              type="text"
              name="firstName"
              value={formData.firstName}
              onChange={handleChange}
              className="input-field"
              placeholder="Seu nome"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-dark mb-1">
              Sobrenome
            </label>
            <input
              type="text"
              name="lastName"
              value={formData.lastName}
              onChange={handleChange}
              className="input-field"
              placeholder="Seu sobrenome"
              required
            />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-dark mb-1">
            Email
          </label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="input-field"
            placeholder="seu@email.com"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-dark mb-1">
            Tipo de Conta
          </label>
          <select
            name="role"
            value={formData.role}
            onChange={handleChange}
            className="input-field"
          >
            <option value="client">Cliente</option>
            <option value="technician">Técnico</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-dark mb-1">
            Senha
          </label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            className="input-field"
            placeholder="Sua senha"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-dark mb-1">
            Confirmar Senha
          </label>
          <input
            type="password"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            className="input-field"
            placeholder="Confirme sua senha"
            required
          />
        </div>

        {error && <div className="text-danger text-sm">{error}</div>}

        <button
          type="submit"
          disabled={isLoading}
          className="btn-primary w-full"
        >
          {isLoading ? "Registrando..." : "Registrar"}
        </button>
      </form>

      <p className="text-center text-gray-600 text-sm mt-6">
        Já tem conta?{" "}
        <Link href="/auth/login" className="text-primary font-medium hover:underline">
          Entre aqui
        </Link>
      </p>
    </div>
  );
}
