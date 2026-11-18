
import { inject } from 'vue';

export default {
  name: 'SummaryCards',

  props: {
    currentPrice: {
      type: Number,
      required: true
    },

    recommendedMarket: {
      type: String,
      required: true
    },

    recommendedDate: {
      type: String,
      required: true
    },

    expectedProfit: {
      type: Number,
      required: true
    },

    predictedPrice: {
      type: Number,
      default: 0
    },

    hasStorage: {
      type: Boolean,
      default: false
    }
  },

  setup() {
    // Access translations provided by App.js
    const i18n = inject('i18n');
    const t = i18n.t;

    function formatINR(val) {
      if (val === undefined || val === null) {
        return '₹0';
      }

      return '₹' + Number(val).toLocaleString('en-IN');
    }

    return {
      t,
      formatINR
    };
  }
};
