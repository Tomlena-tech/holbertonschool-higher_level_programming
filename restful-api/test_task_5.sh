#!/bin/bash

echo "🧪 TESTS COMPLETS DE L'API"
echo "=========================="

USER_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA5NzUyNCwianRpIjoiZTIwMThiMDAtZTlmMy00MzdmLTk4YTAtMmVmMWViMjQ1YzM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIxIiwibmJmIjoxNzYwMDk3NTI0LCJjc3JmIjoiYWYxMjhmYzgtZDY0OC00NWFiLTkwMjktZGY3ZDEyOTRmODQ2IiwiZXhwIjoxNzYwMDk4NDI0LCJyb2xlIjoidXNlciJ9._BUfDJLmrH56oNEkRq08Op1qn0c8LlCCfbztkCfBIEM"

ADMIN_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA5NzY3OCwianRpIjoiN2U1NmUzYWItZTNlYy00MmM0LTg4NDAtM2Y4OTY4NmE1ZWIwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluMSIsIm5iZiI6MTc2MDA5NzY3OCwiY3NyZiI6IjU3ODA5YTA0LWMzNTItNGI4NC04YmNhLTIzZmE1MDUxMjBkYyIsImV4cCI6MTc2MDA5ODU3OCwicm9sZSI6ImFkbWluIn0.0Y-NHQG-VsuHYNemFo0lj8OtOIUSqRC8DESliathngg"

echo ""
echo "✅ Test 1: Basic Auth SANS credentials (doit échouer)"
curl -w "\nHTTP Code: %{http_code}\n" http://127.0.0.1:8000/basic-protected

echo ""
echo "✅ Test 2: Basic Auth AVEC credentials user1"
curl -w "\nHTTP Code: %{http_code}\n" -u user1:password http://127.0.0.1:8000/basic-protected

echo ""
echo "✅ Test 3: Basic Auth AVEC credentials admin1"
curl -w "\nHTTP Code: %{http_code}\n" -u admin1:password http://127.0.0.1:8000/basic-protected

echo ""
echo "✅ Test 4: JWT Protected SANS token (doit échouer)"
curl -w "\nHTTP Code: %{http_code}\n" http://127.0.0.1:8000/jwt-protected

echo ""
echo "✅ Test 5: JWT Protected AVEC token user"
curl -w "\nHTTP Code: %{http_code}\n" http://127.0.0.1:8000/jwt-protected \
  -H "Authorization: Bearer $USER_TOKEN"

echo ""
echo "✅ Test 6: JWT Protected AVEC token admin"
curl -w "\nHTTP Code: %{http_code}\n" http://127.0.0.1:8000/jwt-protected \
  -H "Authorization: Bearer $ADMIN_TOKEN"

echo ""
echo "✅ Test 7: Admin only AVEC token USER (doit échouer - 403)"
curl -w "\nHTTP Code: %{http_code}\n" http://127.0.0.1:8000/admin-only \
  -H "Authorization: Bearer $USER_TOKEN"

echo ""
echo "✅ Test 8: Admin only AVEC token ADMIN (doit réussir)"
curl -w "\nHTTP Code: %{http_code}\n" http://127.0.0.1:8000/admin-only \
  -H "Authorization: Bearer $ADMIN_TOKEN"

echo ""
echo "=========================="
echo "🎉 Tests terminés!"
