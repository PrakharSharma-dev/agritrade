import { computed } from 'vue';

export default {
  name: 'CostAnalysis',
  props: {
    transportCost: {
      type: Number,
      required: true,
      default: 0
    },
    storageCost: {
      type: Number,
      required: true,
      default: 0
    },
    totalCost: {
      type: Number,
      default: null
    }
  },
  setup(props) {
    const computedTotalCost = computed(() => {
      return props.totalCost !== null ? props.totalCost : (props.transportCost + props.storageCost);
    });

    const transportPct = computed(() => {
      if (computedTotalCost.value === 0) return 50;
      return Math.round((props.transportCost / computedTotalCost.value) * 100);
    });

    const storagePct = computed(() => {
      if (computedTotalCost.value === 0) return 50;
      return 100 - transportPct.value;
    });

    function formatINR(val) {
      if (val === undefined || val === null) return '₹0';
      return '₹' + Number(val).toLocaleString('en-IN');
    }

    return {
      computedTotalCost,
      transportPct,
      storagePct,
      formatINR
    };
  }
};
