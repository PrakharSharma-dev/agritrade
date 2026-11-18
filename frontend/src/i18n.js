import { computed, ref } from 'vue';

const STORAGE_KEY = 'agritrade-language';
const locale = ref(localStorage.getItem(STORAGE_KEY) || 'en');

const messages = {
  en: {
    brandTagline: 'Intelligent Agricultural Market Decision & Profit Optimization System',
    portal: 'Portal',
    portalValue: 'Farmer Decision UI',
    farmerAccount: 'Farmer Account',
    logout: 'Logout',
    language: 'Language',
    english: 'English',
    hindi: 'हिन्दी',
    formTitle: 'Find the Best Time & Market to Sell',
    formSubtitle: 'Enter your harvest parameters to discover the most profitable selling strategy',
    selectCrop: 'Select Crop',
    location: 'Your Location / Tehsil',
    quantity: 'Harvest Quantity',
    storage: 'Do you have storage facilities?',
    storageCapacityHint: 'Enter available storage capacity in kg',
    otherExpenses: 'Are there any other expenses?',
    expenseName: 'Expense name',
    expenseCost: 'Expense cost',
    expenseNamePlaceholder: 'e.g. Loading or packaging',
    expenseCostPlaceholder: 'Enter cost in rupees',
    additionalExpenseName: 'Additional Expense Name',
    additionalExpenseNamePlaceholder: 'e.g. Packaging',
    yes: 'Yes',
    no: 'No',
    kg: 'kg',
    quintal: 'Quintal',
    recommendation: 'Get Recommendation',
    analyzing: 'Analyzing Market Conditions...',
    recommendationFailed: 'Recommendation Failed',
    error: 'Unable to generate recommendation. Please try again.',
    tryAgain: 'Try Again',
    clearResults: 'Clear Results',
    showingPlan: 'Showing optimal selling plan for {crop} from {location} ({quantity} kg). Storage available: {storage}.',
    loadingMessage: 'Analyzing market conditions...',
    loadingSubtext: 'Simulating real-time mandi feeds, forecasting 7-day crop price trajectories, and determining logistics & holding costs...',
    emptyTitle: 'Ready to Discover Your Best Selling Opportunity?',
    emptyDescription: 'Select your harvested crop, current location, and quantity above, then click "Get Recommendation" to generate a comprehensive price forecast, candidate mandi comparison, and profit-optimized selling plan.',
    storageAvailable: 'Storage available',
    storageUnavailable: 'No storage available',
    footer: 'AgriTrade • Smart Agricultural Decision Support System',
    footerSubtext: 'Frontend Presentation UI Layer • Connected via Service Layer (Mock / FastAPI Ready)',
    currentPrice: 'Current Market Price',
    recommendedMarket: 'Recommended Market',
    recommendedDate: 'Recommended Selling Date',
    expectedProfit: 'Expected Net Profit',
    optimalPlan: 'OPTIMAL SELLING PLAN',
    systemRecommendation: 'System Recommendation',
    predictedPrice: 'Predicted Selling Price',
    transportCost: 'Estimated Transport Cost',
    storageCost: 'Estimated Storage Cost',
    totalCost: 'Estimated Total Cost',
    storageCapacity: 'Storage Capacity',
    additionalExpense: 'Additional Expense',
    noAdditionalExpense: 'No additional expense',
  },
  hi: {
    brandTagline: 'बुद्धिमान कृषि बाजार निर्णय और लाभ अनुकूलन प्रणाली',
    portal: 'पोर्टल',
    portalValue: 'किसान निर्णय यूआई',
    farmerAccount: 'किसान खाता',
    logout: 'लॉग आउट',
    language: 'भाषा',
    english: 'English',
    hindi: 'हिन्दी',
    formTitle: 'बेचने का सही समय और बाजार खोजें',
    formSubtitle: 'सबसे लाभदायक बिक्री रणनीति जानने के लिए अपनी फसल का विवरण भरें',
    selectCrop: 'फसल चुनें',
    location: 'आपका स्थान / तहसील',
    quantity: 'फसल की मात्रा',
    storage: 'क्या आपके पास भंडारण सुविधा है?',
    storageCapacityHint: 'उपलब्ध भंडारण क्षमता किलोग्राम में भरें',
    otherExpenses: 'क्या कोई अन्य खर्च है?',
    expenseName: 'खर्च का नाम',
    expenseCost: 'खर्च की लागत',
    expenseNamePlaceholder: 'जैसे लोडिंग या पैकेजिंग',
    expenseCostPlaceholder: 'रुपये में लागत भरें',
    additionalExpenseName: 'अतिरिक्त खर्च का नाम',
    additionalExpenseNamePlaceholder: 'जैसे पैकेजिंग',
    yes: 'हां',
    no: 'नहीं',
    kg: 'किलोग्राम',
    quintal: 'क्विंटल',
    recommendation: 'सिफारिश प्राप्त करें',
    analyzing: 'बाजार की स्थितियों का विश्लेषण हो रहा है...',
    recommendationFailed: 'सिफारिश विफल',
    error: 'सिफारिश तैयार नहीं हो सकी। कृपया फिर प्रयास करें।',
    tryAgain: 'फिर प्रयास करें',
    clearResults: 'परिणाम साफ करें',
    showingPlan: '{crop} को {location} से ({quantity} किलोग्राम) बेचने की सर्वोत्तम योजना। भंडारण उपलब्ध: {storage}।',
    loadingMessage: 'बाजार की स्थितियों का विश्लेषण हो रहा है...',
    loadingSubtext: 'वास्तविक समय मंडी डेटा, 7-दिन के मूल्य पूर्वानुमान और लॉजिस्टिक्स लागत का विश्लेषण हो रहा है...',
    emptyTitle: 'अपनी सबसे अच्छी बिक्री का अवसर खोजने के लिए तैयार हैं?',
    emptyDescription: 'ऊपर अपनी फसल, स्थान और मात्रा चुनें, फिर मूल्य पूर्वानुमान और लाभ-अनुकूलित बिक्री योजना के लिए "सिफारिश प्राप्त करें" पर क्लिक करें।',
    storageAvailable: 'भंडारण उपलब्ध',
    storageUnavailable: 'भंडारण उपलब्ध नहीं',
    additionalExpense: 'अन्य खर्च',
    footer: 'एग्रीट्रेड • स्मार्ट कृषि निर्णय सहायता प्रणाली',
    footerSubtext: 'फ्रंटएंड प्रस्तुति परत • सेवा परत से जुड़ी (मॉक / FastAPI तैयार)',
    currentPrice: 'वर्तमान बाजार मूल्य',
    recommendedMarket: 'अनुशंसित बाजार',
    recommendedDate: 'अनुशंसित बिक्री तिथि',
    expectedProfit: 'अनुमानित शुद्ध लाभ',
    optimalPlan: 'सर्वोत्तम बिक्री योजना',
    systemRecommendation: 'सिस्टम सिफारिश',
    predictedPrice: 'अनुमानित बिक्री मूल्य',
    transportCost: 'अनुमानित परिवहन लागत',
    storageCost: 'अनुमानित भंडारण लागत',
    totalCost: 'अनुमानित कुल लागत',
    storageCapacity: 'भंडारण क्षमता',
    additionalExpense: 'अन्य खर्च',
    noAdditionalExpense: 'कोई अन्य खर्च नहीं'
  }
};

export function useI18n() {
  const t = (key, variables = {}) => {
    let value = messages[locale.value]?.[key] || messages.en[key] || key;
    Object.entries(variables).forEach(([name, replacement]) => {
      value = value.replace(`{${name}}`, String(replacement));
    });
    return value;
  };

  function setLocale(nextLocale) {
    if (!messages[nextLocale]) return;
    locale.value = nextLocale;
    localStorage.setItem(STORAGE_KEY, nextLocale);
    document.documentElement.lang = nextLocale === 'hi' ? 'hi' : 'en';
  }

  return { locale: computed(() => locale.value), t, setLocale };
}
