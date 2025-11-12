#!/usr/bin/node
const addButton = document.getElementById('add_item');
const my_list = document.querySelector('ul');
addButton.addEventListener('click', function () {
  const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    my_list.appendChild(newItem);
    });
