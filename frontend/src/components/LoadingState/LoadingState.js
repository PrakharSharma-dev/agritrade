export default {
  name: 'LoadingState',
  props: {
    message: {
      type: String,
      default: 'Analyzing market conditions...'
    },
    subtext: {
      type: String,
      default: 'Evaluating regional APMC mandi forecasts, transportation routes, and holding costs...'
    }
  },
  setup() {
    return {};
  }
};
