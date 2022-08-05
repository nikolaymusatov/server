FROM alpine
WORKDIR script/
RUN apk --no-cache add curl
COPY . .
RUN chmod +x script.sh
CMD ["sh", "script.sh"]