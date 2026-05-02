/**
 * Zustand Store for technician bookings
 */

import { create } from 'zustand';
import { Booking, Technician, Service } from '@/types';
import axiosInstance from '@/lib/api';

interface BookingStore {
  bookings: Booking[];
  technicians: Technician[];
  services: Service[];
  selectedTechnician: Technician | null;
  isLoading: boolean;
  error: string | null;
  fetchTechnicians: (specializationId?: number) => Promise<void>;
  fetchServices: (categoryId?: number, technicianId?: number) => Promise<void>;
  fetchUserBookings: () => Promise<void>;
  createBooking: (bookingData: any) => Promise<void>;
  setSelectedTechnician: (technician: Technician | null) => void;
  clearError: () => void;
}

export const useBookingStore = create<BookingStore>((set) => ({
  bookings: [],
  technicians: [],
  services: [],
  selectedTechnician: null,
  isLoading: false,
  error: null,

  fetchTechnicians: async (specializationId?: number) => {
    set({ isLoading: true, error: null });
    try {
      const params = new URLSearchParams();
      if (specializationId) params.append('specialization_id', specializationId.toString());
      
      const response = await axiosInstance.get(`/technicians?${params}`);
      set({ technicians: response.data, isLoading: false });
    } catch (error: any) {
      set({ error: error.response?.data?.detail || 'Failed to fetch technicians', isLoading: false });
    }
  },

  fetchServices: async (categoryId?: number, technicianId?: number) => {
    set({ isLoading: true, error: null });
    try {
      const params = new URLSearchParams();
      if (categoryId) params.append('category_id', categoryId.toString());
      if (technicianId) params.append('technician_id', technicianId.toString());
      
      const response = await axiosInstance.get(`/services?${params}`);
      set({ services: response.data, isLoading: false });
    } catch (error: any) {
      set({ error: error.response?.data?.detail || 'Failed to fetch services', isLoading: false });
    }
  },

  fetchUserBookings: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await axiosInstance.get('/bookings/my-bookings');
      set({ bookings: response.data, isLoading: false });
    } catch (error: any) {
      set({ error: error.response?.data?.detail || 'Failed to fetch bookings', isLoading: false });
    }
  },

  createBooking: async (bookingData: any) => {
    set({ isLoading: true, error: null });
    try {
      const response = await axiosInstance.post('/bookings', bookingData);
      set((state) => ({ 
        bookings: [...state.bookings, response.data],
        isLoading: false 
      }));
    } catch (error: any) {
      set({ error: error.response?.data?.detail || 'Failed to create booking', isLoading: false });
    }
  },

  setSelectedTechnician: (technician: Technician | null) => {
    set({ selectedTechnician: technician });
  },

  clearError: () => set({ error: null }),
}));
