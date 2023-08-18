document.addEventListener('DOMContentLoaded', () => {
    const quoteElement = document.getElementById('quote');
    const getQuoteBtn = document.getElementById('getQuoteBtn');

    getQuoteBtn.addEventListener('click', async () => {
        try {
            const response = await fetch('/quote');
            const data = await response.json();
            quoteElement.textContent = data.quote;
        } catch (error) {
            console.error('Error fetching quote:', error);
            quoteElement.textContent = 'Failed to fetch quote.';
        }
    });
});
