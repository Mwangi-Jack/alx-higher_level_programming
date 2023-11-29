#include "lists.h"

/**
 * check_cycle - Function
 *
 * Description: This function checks if a cycle exists in a singly linked list
 *
 * @list: a pointer to the first node of the list
 *
 * Return: (0) if there is no cycle, (1) if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	while (ptr2 != NULL && ptr2->next != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
		{
			return (1);
		}

		return (0);
	}
	return (0);
}
