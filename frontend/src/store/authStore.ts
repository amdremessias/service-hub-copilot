/**
 * Zustand Store for authentication
 */

import { create } from 'zustand';
import { User } from '@/types';
import axiosInstance from '@/lib/api';

interface AuthStore {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, firstName: string, lastName: string, role: string) => Promise<void>;
  logout: () => void;
  fetchCurrentUser: () => Promise<void>;
  clearError: () => void;
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  isAuthenticated: false,
  isLoading: false,
  error: null,

  login: async (email: string, password: string) => {
    set({ isLoading: true, error: null });
    try {
      const response = await axiosInstance.post('/auth/login', { email, password });
      const { access_token, refresh_token } = response.data;
      
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('refresh_token', refresh_token);
      
      // Fetch user data
      const userResponse = await axiosInstance.get('/users/me');
      set({ user: userResponse.data, isAuthenticated: true, isLoading: false });
    } catch (error: any) {
      set({ error: error.response?.data?.detail || 'Login failed', isLoading: false });
    }
  },

  register: async (email: string, password: string, firstName: string, lastName: string, role: string) => {
    set({ isLoading: true, error: null });
    try {
      const response = await axiosInstance.post('/auth/register', {
        email,
        password,
        first_name: firstName,
        last_name: lastName,
        role,
      });
      const { access_token, refresh_token } = response.data;
      
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('refresh_token', refresh_token);
      
      // Fetch user data
      const userResponse = await axiosInstance.get('/users/me');
      set({ user: userResponse.data, isAuthenticated: true, isLoading: false });
    } catch (error: any) {
      set({ error: error.response?.data?.detail || 'Registration failed', isLoading: false });
    }
  },

  logout: () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    set({ user: null, isAuthenticated: false });
  },

  fetchCurrentUser: async () => {
    set({ isLoading: true });
    try {
      const response = await axiosInstance.get('/users/me');
      set({ user: response.data, isAuthenticated: true, isLoading: false });
    } catch (error) {
      set({ isAuthenticated: false, isLoading: false });
    }
  },

  clearError: () => set({ error: null }),
}));
