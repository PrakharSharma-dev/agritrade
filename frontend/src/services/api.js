
/**
 * AgriTrade Authentication & API Service Layer
 * Mock authentication and recommendation service.
 * Real ML prediction API integration.
 */

import { MOCK_RECOMMENDATION_RESPONSE } from '../data/mockData';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';
const USE_MOCK = true;

// Generate mock JWT
function createMockJwt(email) {
  const header = btoa(JSON.stringify({ alg: "HS256", typ: "JWT" }));
  const payload = btoa(JSON.stringify({
    sub: email,
    role: "farmer",
    iat: Math.floor(Date.now() / 1000),
    exp: Math.floor(Date.now() / 1000) + (7 * 24 * 60 * 60)
  }));
  const signature = btoa("mock_agritrade_signature_secret");

  return `${header}.${payload}.${signature}`;
}

// Send OTP
export async function sendOtp(email) {
  if (USE_MOCK) {
    return new Promise((resolve) => {
      setTimeout(() => {
        const demoOtp = Math.floor(100000 + Math.random() * 900000).toString();

        resolve({
          success: true,
          otp: demoOtp,
          message: `OTP sent successfully to ${email}`
        });
      }, 600);
    });
  }

  const response = await fetch(`${API_BASE_URL}/auth/send-otp`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });

  if (!response.ok) throw new Error('Unable to send OTP');

  return await response.json();
}

// Verify OTP
export async function verifyOtp(email, otp) {
  if (USE_MOCK) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (!otp || otp.length < 4) {
          reject(new Error('Invalid OTP. Please check and enter the 6-digit code.'));
          return;
        }

        const token = createMockJwt(email);

        localStorage.setItem('agritrade_jwt_token', token);
        localStorage.setItem('agritrade_user_email', email);

        resolve({
          access_token: token,
          token_type: 'bearer',
          user: { email, role: 'farmer' }
        });
      }, 600);
    });
  }

  const response = await fetch(`${API_BASE_URL}/auth/verify-otp`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, otp })
  });

  if (!response.ok) throw new Error('Authentication failed');

  const data = await response.json();

  localStorage.setItem('agritrade_jwt_token', data.access_token);
  localStorage.setItem('agritrade_user_email', email);

  return data;
}

// Get stored authentication
export function getStoredAuth() {
  const token = localStorage.getItem('agritrade_jwt_token');
  const email = localStorage.getItem('agritrade_user_email');

  return {
    isAuthenticated: !!token,
    token,
    email
  };
}

// Logout
export function logoutUser() {
  localStorage.removeItem('agritrade_jwt_token');
  localStorage.removeItem('agritrade_user_email');
}

// Existing mock recommendation service
export async function getRecommendation(payload) {
  if (USE_MOCK) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({
          ...MOCK_RECOMMENDATION_RESPONSE,
          crop: payload.crop || MOCK_RECOMMENDATION_RESPONSE.crop,
          farmer_location: payload.location || MOCK_RECOMMENDATION_RESPONSE.farmer_location,
          quantity: payload.quantity || MOCK_RECOMMENDATION_RESPONSE.quantity
        });
      }, 750);
    });
  }

  const token = localStorage.getItem('agritrade_jwt_token');

  const response = await fetch(`${API_BASE_URL}/recommendation`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': token ? `Bearer ${token}` : ''
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    throw new Error(`Backend error: ${response.statusText}`);
  }

  return await response.json();
}

// NEW: Real ML prediction API
export async function getPrediction(cropId, marketId) {
  const url = new URL(`${API_BASE_URL}/api/predictions/`);

  url.searchParams.append('crop_id', cropId);
  url.searchParams.append('market_id', marketId);

  const response = await fetch(url);

  if (!response.ok) {
    let message = `Prediction API error: ${response.status}`;

    try {
      const errorData = await response.json();
      message = errorData.detail || message;
    } catch {
      // Keep default error message
    }

    throw new Error(message);
  }

  return await response.json();
}
