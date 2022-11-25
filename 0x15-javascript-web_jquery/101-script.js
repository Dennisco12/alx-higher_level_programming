#!/usr/bin/node
window.onload () => {
	const add = $('DIV#add_item');
	const remove = $('DIV#remove_item');
	const clear = $('DIV#clear_list');

	add.click(() => {
		$('UL.my_list').append('<li>Item</li>');
	} remove.click(() => {
		const last = $('UL.my_list').last();
		last.remove();
	} clear.click(() => {
		$('UL.my_list').text("")
	};
};
