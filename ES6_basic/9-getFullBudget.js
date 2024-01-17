import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  return {
    full_income:'$${income}\n${income} euros'
  };
}
