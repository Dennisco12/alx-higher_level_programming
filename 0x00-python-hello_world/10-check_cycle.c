#include "lists.h"

/**
 * check_cycle - A function that checks for cycles in a singly linked list
 * @list: The list to be checked
 * Return: 1 if cycle is present, and 0 if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *node;
	listint_t *front;

	node = list;
	front = list;

	while(node && front && front->next)
	{
		node = node->next;
		front = (front->next)->next;
		if (front == node)
			return (1);
	}

	return (0);
}
