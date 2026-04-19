// affiliate-protect.js

(function() {
    // Define your affiliate link and ID
    const affiliateLink = 'https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885';
    const affiliateLinkElement = document.querySelector('#affiliate-link');

    // Ensure the affiliate link is valid and unmodified
    if (affiliateLinkElement) {
        affiliateLinkElement.href = affiliateLink;
    }

    // Function to set a cookie to track the affiliate ID
    function setAffiliateCookie() {
        // Set a cookie with the affiliate ID and current timestamp
        const expires = new Date();
        expires.setTime(expires.getTime() + (30 * 24 * 60 * 60 * 1000)); // Cookie expires in 30 days
        document.cookie = "affiliate_id=21885; expires=" + expires.toUTCString() + "; path=/";
    }

    // Check if the affiliate ID cookie is already set
    function checkAffiliateCookie() {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith("affiliate_id=")) {
                return true; // Affiliate cookie already set
            }
        }
        return false; // Affiliate cookie not found
    }

    // If the affiliate cookie isn't set, set it and track the user
    if (!checkAffiliateCookie()) {
        setAffiliateCookie();
    }

    // Optionally, you can use localStorage or sessionStorage to track the user's visit more securely
    // Store the affiliate ID in localStorage if not already stored
    if (!localStorage.getItem('affiliate_id')) {
        localStorage.setItem('affiliate_id', '21885');
    }

    // Monitor the click event to ensure tracking occurs
    if (affiliateLinkElement) {
        affiliateLinkElement.addEventListener('click', function() {
            console.log('Affiliate link clicked');
            // Here, you can add additional tracking or analytics if necessary
        });
    }

})();
