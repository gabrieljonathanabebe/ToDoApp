// mytodo/clients/web/src/hooks/usePagination.js

import { useState } from "react";


export function usePagination(items, itemsPerPage = 5) {
  const [requestedPage, setPage] = useState(1)
  const totalPages = Math.ceil(items.length / itemsPerPage)
  const page = Math.min(requestedPage, totalPages || 1)
  const startIndex = (page - 1) * itemsPerPage
  const paginatedItems = items.slice(startIndex, startIndex + itemsPerPage)

  function goPrevious() {
    if (page > 1) setPage(page - 1)
  }

  function goNext() {
    if (page < totalPages) setPage(page + 1)
  }

  return {
    page,
    totalPages,
    paginatedItems,
    goPrevious,
    goNext,
    setPage,
  }
}
