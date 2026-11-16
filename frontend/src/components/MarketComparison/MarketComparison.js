export default {
  name: 'MarketComparison',
  props: {
    markets: {
      type: Array,
      required: true,
      default: () => []
    },
    recommendedMarketName: {
      type: String,
      default: ''
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
