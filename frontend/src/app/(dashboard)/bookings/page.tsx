"use client";

import { useBookingStore } from "@/store/bookingStore";
import { useEffect } from "react";

export default function BookingsPage() {
  const { bookings, fetchUserBookings, isLoading } = useBookingStore();

  useEffect(() => {
    fetchUserBookings();
  }, []);

  return (
    <div>
      <h1 className="text-4xl font-bold mb-8">Meus Agendamentos</h1>
      
      {isLoading ? (
        <p className="text-gray-600">Carregando agendamentos...</p>
      ) : bookings.length === 0 ? (
        <div className="card text-center py-12">
          <p className="text-gray-600 mb-4">Você ainda não tem agendamentos</p>
          <a href="/services" className="btn-primary inline-block">
            Ver Serviços
          </a>
        </div>
      ) : (
        <div className="space-y-4">
          {bookings.map((booking) => (
            <div key={booking.id} className="card">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-lg font-semibold mb-2">Agendamento #{booking.id}</h3>
                  <p className="text-gray-600">
                    Data: {new Date(booking.scheduled_date).toLocaleDateString('pt-BR')}
                  </p>
                  <p className="text-gray-600">Local: {booking.address}</p>
                  <p className="text-gray-600">Duração: {booking.duration_minutes} minutos</p>
                </div>
                <div className="text-right">
                  <span className={`inline-block px-3 py-1 rounded-full text-sm font-semibold ${
                    booking.status === 'completed' ? 'bg-success text-white' :
                    booking.status === 'cancelled' ? 'bg-danger text-white' :
                    booking.status === 'confirmed' ? 'bg-primary text-white' :
                    'bg-warning text-white'
                  }`}>
                    {booking.status.charAt(0).toUpperCase() + booking.status.slice(1)}
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
