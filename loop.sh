while true
do
./<PATH_TO_SCRIPT>
echo "this is the try: ${LOOP_COUNT}"

if [ "$LOOP_COUNT" -gt 2500 ]
then
  break
fi

LOOP_COUNT=$(($LOOP_COUNT+1))
sleep 5
done
