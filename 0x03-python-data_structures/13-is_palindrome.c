#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * reverseList - function
 *
 * Description: This function reverses a linked list
 *
 * @head: pointer to first node of the linked list
 *
 * Return: returns a pointer to the first node of the reversed linked list
 *
*/
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - function
 *
 * Description: this function checks if a linked list is a palindrome
 *
 * @head: a pointer to pointer to head of the linked list
 *
 * Return: (0) if is not a palindrome or (1), if is palindrome (1)
*/

int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = *head;
	listint_t *ptr2 = reverseList(*head);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (ptr1->next != NULL && ptr2->next != NULL)
	{
		if (ptr1->n != ptr2->n)
		{
			return (0);
			exit(0);
		}
	}

	return (1);
}
