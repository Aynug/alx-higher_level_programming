#include "lists.h"

int _is_palindrome(listint_t **head, listint_t *tail)
{
	int status = 1;

	if (tail)
	{
		status = _is_palindrome(head, tail->next);

		if (tail == *head || tail->next == *head)
			*head = tail;
		else if (status && (*head)->n == tail->n)
			*head = (*head)->next;
		else
			status = 0;
	}
	return (status);
}
int is_palindrome(listint_t **head)
{
	return (head && _is_palindrome(head, *head));
}
