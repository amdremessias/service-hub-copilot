/**
 * Type definitions for the application
 */

export interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  phone?: string;
  profile_picture?: string;
  bio?: string;
  role: 'client' | 'technician' | 'admin';
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
  updated_at: string;
}

export interface Technician {
  id: number;
  user_id: number;
  company_name?: string;
  bio?: string;
  years_of_experience: number;
  rating: number;
  total_reviews: number;
  hourly_rate: number;
  is_verified: number;
  specializations: Specialization[];
  created_at: string;
  updated_at: string;
}

export interface Specialization {
  id: number;
  name: string;
  description?: string;
  created_at: string;
}

export interface Service {
  id: number;
  technician_id: number;
  category_id: number;
  title: string;
  description: string;
  price: number;
  duration_minutes: number;
  is_available: boolean;
  image_url?: string;
  created_at: string;
  updated_at: string;
}

export interface ServiceCategory {
  id: number;
  name: string;
  description?: string;
  icon_url?: string;
  created_at: string;
}

export interface Booking {
  id: number;
  client_id: number;
  technician_id: number;
  service_id: number;
  scheduled_date: string;
  duration_minutes: number;
  address: string;
  notes?: string;
  status: 'pending' | 'confirmed' | 'in_progress' | 'completed' | 'cancelled' | 'no_show';
  latitude?: string;
  longitude?: string;
  created_at: string;
  updated_at: string;
}

export interface Review {
  id: number;
  booking_id: number;
  reviewer_id: number;
  technician_id: number;
  rating: number;
  comment?: string;
  professionalism?: number;
  punctuality?: number;
  quality?: number;
  created_at: string;
  updated_at: string;
}

export interface Payment {
  id: number;
  booking_id: number;
  user_id: number;
  amount: number;
  status: 'pending' | 'processing' | 'completed' | 'failed' | 'refunded';
  stripe_payment_id?: string;
  payment_method?: string;
  created_at: string;
  updated_at: string;
}

export interface ChatRoom {
  id: number;
  client_id: number;
  technician_id: number;
  booking_id?: number;
  created_at: string;
  updated_at: string;
  messages?: ChatMessage[];
}

export interface ChatMessage {
  id: number;
  chat_room_id: number;
  sender_id: number;
  content: string;
  is_read: number;
  created_at: string;
}
