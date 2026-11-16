export default {
  name: 'OptimalPlanCard',
  props: {
    recommendation: {
      type: Object,
      required: true
    },
    crop: {
      type: String,
      default: 'Wheat'
    },
    quantity: {
      type: Number,
      default: 1000
    }
  },
  setup() {
    function formatINR(val) {
      if (val === undefined || val === null) return '₹0';
      return '₹' + Number(val).toLocaleString('en-IN');
    }

    return {
      formatINR
    };
  }
};
