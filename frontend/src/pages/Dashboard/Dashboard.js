import { ref, computed, inject } from 'vue';

import Header from '../../components/Header/Header.vue';
import FarmerInput from '../../components/FarmerInput/FarmerInput.vue';
import SummaryCards from '../../components/SummaryCards/SummaryCards.vue';
import OptimalPlanCard from '../../components/OptimalPlanCard/OptimalPlanCard.vue';
import ForecastChart from '../../components/ForecastChart/ForecastChart.vue';
import MarketComparison from '../../components/MarketComparison/MarketComparison.vue';
import CostAnalysis from '../../components/CostAnalysis/CostAnalysis.vue';
import LoadingState from '../../components/LoadingState/LoadingState.vue';
import EmptyState from '../../components/EmptyState/EmptyState.vue';
import ChatBot from '../../components/ChatBot/ChatBot.vue';

import {
  getRecommendation,
  getPrediction
} from '../../services/api';

export default {
  name: 'Dashboard',

  components: {
    Header,
    FarmerInput,
    SummaryCards,
    OptimalPlanCard,
    ForecastChart,
    MarketComparison,
    CostAnalysis,
    LoadingState,
    EmptyState,
    ChatBot
  },

  props: {
    userEmail: {
      type: String,
      default: ''
    }
  },

  emits: ['logout'],

  setup(props, { emit }) {
    const { t } = inject('i18n');

    const loading = ref(false);
    const error = ref(null);
    const predictionError = ref(null);

    const resultData = ref(null);
    const predictionData = ref(null);
    const lastQueryParams = ref(null);

    // Chatbot context
    const chatContext = computed(() => ({
      resultData: resultData.value,
      queryParams: lastQueryParams.value
    }));

    // Verified database IDs
    const cropIdMap = {
      Wheat: 1
    };

    const marketIdMap = {
      Ajmer: 1
    };

    async function handleFarmerSubmit(queryParams) {
      loading.value = true;
      error.value = null;
      predictionError.value = null;

      resultData.value = null;
      predictionData.value = null;
      lastQueryParams.value = queryParams;

      try {
        // Existing recommendation functionality
        const recommendationPromise = getRecommendation(queryParams);

        // ML prediction functionality
        const cropId = cropIdMap[queryParams.crop];
        const marketId = marketIdMap[queryParams.location];

        let predictionPromise;

        if (cropId && marketId) {
          predictionPromise = getPrediction(cropId, marketId);
        } else {
          predictionPromise = Promise.reject(
            new Error(
              'Real prediction is currently configured only for Wheat and Ajmer.'
            )
          );
        }

        // Run both requests independently
        const [recommendationResult, predictionResult] =
          await Promise.allSettled([
            recommendationPromise,
            predictionPromise
          ]);

        if (recommendationResult.status === 'fulfilled') {
          resultData.value = recommendationResult.value;
        } else {
          throw recommendationResult.reason;
        }

        if (predictionResult.status === 'fulfilled') {
          predictionData.value = predictionResult.value;
        } else {
          console.error('Prediction API Error:', predictionResult.reason);

          predictionError.value =
            predictionResult.reason?.message ||
            'Prediction service unavailable.';
        }

      } catch (err) {
        console.error('Dashboard Error:', err);
        error.value = t('error');

      } finally {
        loading.value = false;
      }
    }

    function handleRetry() {
      if (lastQueryParams.value) {
        handleFarmerSubmit(lastQueryParams.value);
      }
    }

    function handleReset() {
      resultData.value = null;
      predictionData.value = null;
      predictionError.value = null;
      error.value = null;
    }

    function handleLogout() {
      emit('logout');
    }

    return {
      loading,
      error,
      predictionError,
      resultData,
      predictionData,
      lastQueryParams,
      handleFarmerSubmit,
      handleRetry,
      handleReset,
      handleLogout,
      chatContext,
      t
    };
  }
};