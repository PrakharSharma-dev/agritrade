import { ref } from 'vue';
import { AVAILABLE_CROPS, AVAILABLE_LOCATIONS } from '../../data/mockData';

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
    const selectedCrop = ref('Wheat');
    const selectedLocation = ref('Ajmer');
    const quantity = ref(1000); // in kg
    const unit = ref('kg'); // kg or quintal

    function handleSubmit() {
      const quantityInKg = unit.value === 'quintal' ? quantity.value * 100 : quantity.value;
      emit('submit-query', {
        crop: selectedCrop.value,
        location: selectedLocation.value,
        quantity: quantityInKg,
        unit: unit.value
      });
    }

    return {
      AVAILABLE_CROPS,
      AVAILABLE_LOCATIONS,
      selectedCrop,
      selectedLocation,
      quantity,
      unit,
      handleSubmit
    };
  }
};
