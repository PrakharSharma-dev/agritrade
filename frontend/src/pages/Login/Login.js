import { ref } from 'vue';
import { sendOtp, verifyOtp } from '../../services/api';

export default {
  name: 'Login',
  emits: ['login-success'],
  setup(props, { emit }) {
    const email = ref('farmer.ramesh@agritrade.in');
    const enteredOtp = ref('');
    const currentOtp = ref('');
    const showOtpOverlay = ref(false);
    const loading = ref(false);
    const verifying = ref(false);
    const errorMessage = ref(null);
    const otpError = ref(null);

    async function handleSendOtp() {
      if (!email.value) return;
      loading.value = true;
      errorMessage.value = null;

      try {
        const response = await sendOtp(email.value);
        currentOtp.value = response.otp;
        enteredOtp.value = '';
        otpError.value = null;
        showOtpOverlay.value = true;
      } catch (err) {
        console.error('OTP Send Error:', err);
        errorMessage.value = 'Failed to generate OTP. Please try again.';
      } finally {
        loading.value = false;
      }
    }

    async function handleVerifyOtp() {
      if (!enteredOtp.value) return;
      verifying.value = true;
      otpError.value = null;

      try {
        const result = await verifyOtp(email.value, enteredOtp.value);
        showOtpOverlay.value = false;
        emit('login-success', {
          token: result.access_token,
          email: email.value
        });
      } catch (err) {
        console.error('OTP Verification Error:', err);
        otpError.value = err.message || 'Invalid OTP code entered. Please check the code above.';
      } finally {
        verifying.value = false;
      }
    }

    function autoFillOtp() {
      if (currentOtp.value) {
        enteredOtp.value = currentOtp.value;
      }
    }

    function resendOtp() {
      handleSendOtp();
    }

    function closeOtpModal() {
      showOtpOverlay.value = false;
      otpError.value = null;
    }

    return {
      email,
      enteredOtp,
      currentOtp,
      showOtpOverlay,
      loading,
      verifying,
      errorMessage,
      otpError,
      handleSendOtp,
      handleVerifyOtp,
      autoFillOtp,
      resendOtp,
      closeOtpModal
    };
  }
};
