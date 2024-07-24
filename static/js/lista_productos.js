document.addEventListener('DOMContentLoaded', function() {
    const url = new URL(window.location.href);
    const selectedValue = url.searchParams.get('order')
    if (selectedValue) {
        const selectElement = document.getElementById('order_select')
        selectElement.value = selectedValue;
    }
});

document.getElementById('order_select').addEventListener('change', function() {
    const selectedValue = this.value;
    if (selectedValue && selectedValue !== '---') {
        const currentUrl = window.location.href;
        const url = new URL(currentUrl)
        url.searchParams.set('order', selectedValue)
        window.location.href = url.toString();
    } else if (selectedValue === '---') {
        const currentUrl = window.location.href;
        const url = new URL(currentUrl)
        url.searchParams.delete('order')
        window.location.href = url.toString();
    }
})

