async function showStatus() {
    const msgDiv = document.getElementById('message');
    try {
        const { lastError } = await chrome.storage.local.get('lastError');
        if (lastError) {
            msgDiv.innerHTML = `❌ Error: ${lastError}<br>Please try the authentication again.`;
            msgDiv.classList.add('error');
        } else {
            msgDiv.innerHTML = '✅ Ready. Start OAuth authentication in your Home Assistant.';
            msgDiv.classList.add('success');
        }
    } catch (e) {
        msgDiv.innerHTML = '⚠️ Could not read status.';
    }
}

document.getElementById('githubBtn').addEventListener('click', () => {
    chrome.tabs.create({ url: 'https://github.com/sander1988/indego/issues' });
});

showStatus();