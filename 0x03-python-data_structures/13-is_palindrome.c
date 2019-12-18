#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse_listint - function that reverses a listint_t linked list.
 * @head: address of a pointer to a structure of type listint_t
 *
 * Return: a pointer to the first node of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - verify if list is palindrome
 * @head: address of a pointer to a structure of type listint_t
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *reve = *head, *temp = *head;

	if (*head == NULL)
		return (1);

	while (temp && temp->next && temp->next->next)
	{
		reve = reve->next;
		temp = temp->next->next;
	}

	reve = reverse_listint(&reve);
	temp = *head;

	while (temp != NULL && reve != NULL)
	{
		if ((*temp).n != (*reve).n)
		{
			free_listint(reve);
			return (0);
		}
		temp = (*temp).next;
		reve = (*reve).next;
	}
	free_listint(reve);
	return (1);
}
