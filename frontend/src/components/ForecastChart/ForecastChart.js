import { ref, computed } from 'vue';

export default {
  name: 'ForecastChart',
  props: {
    forecastData: {
      type: Array,
      required: true,
      default: () => []
    },
    recommendedDate: {
      type: String,
      default: ''
    }
  },
  setup(props) {
    const hoveredIndex = ref(null);

    const prices = computed(() => props.forecastData.map(d => d.predicted_price));
    const minPrice = computed(() => Math.min(...prices.value, 2300) - 30);
    const maxPrice = computed(() => Math.max(...prices.value, 2550) + 30);
    const priceRange = computed(() => maxPrice.value - minPrice.value || 1);

    // SVG dimensions
    const svgWidth = 700;
    const svgHeight = 280;
    const padding = { top: 30, right: 30, bottom: 40, left: 55 };

    const chartWidth = computed(() => svgWidth - padding.left - padding.right);
    const chartHeight = computed(() => svgHeight - padding.top - padding.bottom);

    // Point coordinates
    const points = computed(() => {
      if (!props.forecastData.length) return [];
      const stepX = chartWidth.value / (props.forecastData.length - 1);
      return props.forecastData.map((d, index) => {
        const x = padding.left + index * stepX;
        const yRatio = (d.predicted_price - minPrice.value) / priceRange.value;
        const y = padding.top + chartHeight.value - (yRatio * chartHeight.value);
        return {
          ...d,
          index,
          x,
          y
        };
      });
    });

    // SVG Path generator for smooth curve
    const linePath = computed(() => {
      if (points.value.length === 0) return '';
      return points.value.reduce((acc, point, i, arr) => {
        if (i === 0) return `M ${point.x},${point.y}`;
        const prev = arr[i - 1];
        const cpX = (prev.x + point.x) / 2;
        return `${acc} C ${cpX},${prev.y} ${cpX},${point.y} ${point.x},${point.y}`;
      }, '');
    });

    // Area fill path
    const areaPath = computed(() => {
      if (points.value.length === 0) return '';
      const first = points.value[0];
      const last = points.value[points.value.length - 1];
      const bottomY = padding.top + chartHeight.value;
      return `${linePath.value} L ${last.x},${bottomY} L ${first.x},${bottomY} Z`;
    });

    // Y-Axis Ticks (4 ticks)
    const yTicks = computed(() => {
      const count = 4;
      const step = priceRange.value / count;
      return Array.from({ length: count + 1 }, (_, i) => {
        const val = Math.round(minPrice.value + step * i);
        const y = padding.top + chartHeight.value - ((val - minPrice.value) / priceRange.value * chartHeight.value);
        return { val, y };
      });
    });

    // Max price point
    const peakPoint = computed(() => {
      if (!points.value.length) return null;
      return points.value.reduce((max, p) => p.predicted_price > max.predicted_price ? p : max, points.value[0]);
    });

    function formatINR(val) {
      if (val === undefined || val === null) return '₹0';
      return '₹' + Number(val).toLocaleString('en-IN');
    }

    return {
      hoveredIndex,
      svgWidth,
      svgHeight,
      padding,
      chartWidth,
      chartHeight,
      points,
      linePath,
      areaPath,
      yTicks,
      peakPoint,
      formatINR
    };
  }
};
