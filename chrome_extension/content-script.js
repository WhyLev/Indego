const urlRegex = /"com\.bosch\.indegoconnect%3a%2f%2flogin(.*?)"/;

let result = document.body.innerHTML.match(urlRegex);
if (result && result[1]) {
    let redirectUrl = "https://my.home-assistant.io/redirect/oauth" + decodeURIComponent(result[1]);
    console.log("Redirecting to HA", redirectUrl);
    window.location.href = redirectUrl;
} else {
    console.warn("No OAuth code found in HTML.");
    chrome.storage.local.set({ lastError: "No valid OAuth link found in the response." });
}