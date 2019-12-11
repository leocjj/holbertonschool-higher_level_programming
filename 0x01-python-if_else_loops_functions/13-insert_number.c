#include <stdlib.h>
#include "lists.h"
/**
 * insert_nodeint_at_index - inserts a new node at a given position.
 * @head: address of a pointer to a structure of type listint_t
 * @idx: index of the list where the new node should be added. Index starts: 0
 * @n: data for inserted node
 *
 * Return: the address of the new node, or NULL if it failed. If it is not
 * possible to add the new node at index idx, do not add and return NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp_node = *head, *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else if (number < temp_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (temp_node->next != NULL)
		{
			if ((*(temp_node->next)).n < number)
				temp_node = temp_node->next;
			else
				break;
		}

		new_node->next = temp_node->next;
		temp_node->next = new_node;
	}
	return (new_node);
}
