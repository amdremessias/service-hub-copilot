"use client";

import { useBookingStore } from "@/store/bookingStore";
import { useEffect } from "react";

export default function ServicesPage() {
  const { services, technicians, fetchServices, fetchTechnicians, isLoading } = useBookingStore();

  useEffect(() => {
    fetchServices();
    fetchTechnicians();
  }, []);

  return (
    <div>
      <h1 className="text-4xl font-bold mb-8">Serviços Disponíveis</h1>
      
      {isLoading ? (
        <p className="text-gray-600">Carregando serviços...</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {services.map((service) => (
            <div key={service.id} className="card hover:shadow-lg transition-shadow">
              {service.image_url && (
                <img
                  src={service.image_url}
                  alt={service.title}
                  className="w-full h-48 object-cover rounded-lg mb-4"
                />
              )}
              <h3 className="text-xl font-semibold mb-2">{service.title}</h3>
              <p className="text-gray-600 text-sm mb-4">{service.description}</p>
              <div className="flex justify-between items-center">
                <span className="text-2xl font-bold text-primary">R$ {service.price.toFixed(2)}</span>
                <span className="text-sm text-gray-600">{service.duration_minutes} min</span>
              </div>
              <button className="btn-primary w-full mt-4">
                Agendar
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
