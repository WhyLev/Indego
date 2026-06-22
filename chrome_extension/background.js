const CUSTOM_RULE_ID = 1

chrome.declarativeNetRequest.updateDynamicRules({
    removeRuleIds: [CUSTOM_RULE_ID],
    addRules: [
        {
            id: CUSTOM_RULE_ID,
            priority: 1,
            action: {
                type: "modifyHeaders",
                responseHeaders: [ {
                    operation: "remove",
                    header: "Location"
                } ]
            },
            condition: {
                "urlFilter": "|https://prodindego.b2clogin.com/prodindego.onmicrosoft.com/oauth2/authresp|",
                "resourceTypes": ["main_frame"]
            },
        }
    ],
});
