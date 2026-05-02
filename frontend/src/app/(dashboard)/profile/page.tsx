"use client";

import { useAuthStore } from "@/store/authStore";
import { useState, useEffect } from "react";
import toast from "react-hot-toast";
import axiosInstance from "@/lib/api";

export default function ProfilePage() {
  const { user, fetchCurrentUser } = useAuthStore();
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    phone: "",
    bio: "",
  });

  useEffect(() => {
    if (user) {
      setFormData({
        first_name: user.first_name,
        last_name: user.last_name,
        phone: user.phone || "",
        bio: user.bio || "",
      });
    }
  }, [user]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axiosInstance.put("/users/me", formData);
      toast.success("Perfil atualizado com sucesso!");
      fetchCurrentUser();
      setIsEditing(false);
    } catch (error) {
      toast.error("Erro ao atualizar perfil");
    }
  };

  return (
    <div>
      <h1 className="text-4xl font-bold mb-8">Meu Perfil</h1>
      
      {user && (
        <div className="card max-w-2xl">
          {!isEditing ? (
            <div>
              <div className="mb-6">
                <h3 className="text-lg font-semibold mb-2">Informações Pessoais</h3>
                <p className="text-gray-600"><strong>Nome:</strong> {user.first_name} {user.last_name}</p>
                <p className="text-gray-600"><strong>Email:</strong> {user.email}</p>
                <p className="text-gray-600"><strong>Telefone:</strong> {user.phone || "Não informado"}</p>
                <p className="text-gray-600"><strong>Bio:</strong> {user.bio || "Não informado"}</p>
              </div>
              <button
                onClick={() => setIsEditing(true)}
                className="btn-primary"
              >
                Editar Perfil
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-dark mb-1">
                    Nome
                  </label>
                  <input
                    type="text"
                    name="first_name"
                    value={formData.first_name}
                    onChange={handleChange}
                    className="input-field"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-dark mb-1">
                    Sobrenome
                  </label>
                  <input
                    type="text"
                    name="last_name"
                    value={formData.last_name}
                    onChange={handleChange}
                    className="input-field"
                  />
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-dark mb-1">
                  Telefone
                </label>
                <input
                  type="tel"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                  className="input-field"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-dark mb-1">
                  Bio
                </label>
                <textarea
                  name="bio"
                  value={formData.bio}
                  onChange={handleChange}
                  className="input-field"
                  rows={4}
                />
              </div>

              <div className="flex gap-4">
                <button type="submit" className="btn-primary">
                  Salvar
                </button>
                <button
                  type="button"
                  onClick={() => setIsEditing(false)}
                  className="btn-outline"
                >
                  Cancelar
                </button>
              </div>
            </form>
          )}
        </div>
      )}
    </div>
  );
}
