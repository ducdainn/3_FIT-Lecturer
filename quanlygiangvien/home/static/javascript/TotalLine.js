
const containerNumberTotal = document.createElement('div');
containerNumberTotal.className = 'container_numberTotal';

ARRAY_LIST_NUMBER_TOTAL.forEach(item => {
    const itemTotalNumber = document.createElement('div');
    itemTotalNumber.className = 'item_total_number';
    itemTotalNumber.setAttribute('key', item.id);

    const iconContainer = document.createElement('div');
    const iconElement = document.createElement('span');
    iconElement.innerHTML = item.iconTotal;
    iconContainer.appendChild(iconElement);

    const textContainer = document.createElement('div');
    textContainer.className = 'text_total';
    textContainer.textContent = item.textTotal;

    const numberContainer = document.createElement('div');
    numberContainer.className = 'number_total';
    numberContainer.textContent = item.number;

    const numberTotalContainer = document.createElement('div');
    numberTotalContainer.appendChild(textContainer);
    numberTotalContainer.appendChild(numberContainer);

    itemTotalNumber.appendChild(iconContainer);
    itemTotalNumber.appendChild(numberTotalContainer);

    containerNumberTotal.appendChild(itemTotalNumber);
});

// Để hiển thị kết quả, bạn có thể thêm containerNumberTotal vào phần tử gốc của DOM
document.getElementById('total_line').appendChild(containerNumberTotal);