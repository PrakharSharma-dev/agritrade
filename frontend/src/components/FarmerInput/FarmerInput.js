
import { ref, inject } from 'vue';
import {
  AVAILABLE_CROPS,
  AVAILABLE_LOCATIONS
} from '../../data/mockData';

export default {
  name: 'FarmerInput',

  props: {
    loading: {
      type: Boolean,
      default: false
    }
  },

  emits: ['submit-query'],

  setup(props, { emit }) {
    // Existing farmer inputs
    const selectedCrop = ref('Wheat');
    const selectedLocation = ref('Ajmer');
    const quantity = ref(1000);
    const unit = ref('kg');

    // Additional farmer inputs
    const hasStorage = ref(null);
    const transportationCost = ref(null);
    const storageCost = ref(null);
    const additionalExpenseName = ref('');
    const additionalExpenseCost = ref(null);

    // Internationalization
    const { t } = inject('i18n');

    function handleSubmit() {
      // Validate storage selection
      if (hasStorage.value === null) return;

      // Validate transportation cost
      if (
        transportationCost.value === null ||
        transportationCost.value < 0
      ) return;

      // Validate storage cost when storage is available
      if (
        hasStorage.value &&
        (storageCost.value === null || storageCost.value < 0)
      ) return;

      // Validate additional expense
      if (!additionalExpenseName.value.trim()) return;

      if (
        additionalExpenseCost.value === null ||
        additionalExpenseCost.value < 0
      ) return;

      // Convert quantity into kilograms
      const quantityInKg =
        unit.value === 'quintal'
          ? quantity.value * 100
          : quantity.value;

      // Submit all farmer inputs to Dashboard
      emit('submit-query', {
        crop: selectedCrop.value,
        location: selectedLocation.value,
        quantity: quantityInKg,
        unit: unit.value,

        has_storage: hasStorage.value,
        transport_cost: Number(transportationCost.value),
        storage_cost: hasStorage.value
          ? Number(storageCost.value)
          : 0,

        additional_expense_name:
          additionalExpenseName.value.trim(),

        additional_expense_cost:
          Number(additionalExpenseCost.value)
      });
    }

    return {
      AVAILABLE_CROPS,
      AVAILABLE_LOCATIONS,

      selectedCrop,
      selectedLocation,
      quantity,
      unit,

      hasStorage,
      transportationCost,
      storageCost,
      additionalExpenseName,
      additionalExpenseCost,

      t,
      handleSubmit
    };
  }
};
