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
	listint_t *reve = NULL, *temp = NULL;

	temp = *head;
	while (temp != NULL)
	{
		add_nodeint_end(&reve, temp->n);
		if ((*temp).next != NULL)
			temp = (*temp).next;
		else
			break;
	}

	reve = reverse_listint(&reve);
	print_listint(reve);

	temp = *head;
	while (temp != NULL)
	{
		if ((*temp).n != (*reve).n)
			return (0);
		temp = (*temp).next;
		reve = (*reve).next;
	}
	return (1);
}
