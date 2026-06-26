const CUSTOM_RULE_ID = 1;

async function updateNetRules() {
    try {
        await chrome.declarativeNetRequest.updateDynamicRules({
            removeRuleIds: [CUSTOM_RULE_ID],
            addRules: [
                {
                    id: CUSTOM_RULE_ID,
                    priority: 1,
                    action: {
                        type: "modifyHeaders",
                        responseHeaders: [{
                            operation: "remove",
                            header: "Location"
                        }]
                    },
                    condition: {
                        urlFilter: "|https://prodindego.b2clogin.com/prodindego.onmicrosoft.com/oauth2/authresp|",
                        resourceTypes: ["main_frame"]
                    }
                }
            ]
        });
        await chrome.storage.local.set({ lastError: null });
    } catch (error) {
        console.error("Failed to set rule:", error);
        await chrome.storage.local.set({ lastError: error.message });
    }
}

updateNetRules();

// Optional: listen for web request errors (not supported in all browsers, safe to keep)
if (chrome.webRequest) {
    chrome.webRequest.onErrorOccurred.addListener(
        async (details) => {
            if (details.url.includes("prodindego.b2clogin.com")) {
                await chrome.storage.local.set({ lastError: details.error });
            }
        },
        { urls: ["https://prodindego.b2clogin.com/*"] }
    );
}