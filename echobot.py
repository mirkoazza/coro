require 'telegramAPI'
token = "153778554:AAFaF8k88PA3fL10BP6nlV6oFY1VPFLxyuo"
api = TelegramAPI.new token
while true do
 # Get last messages if there are, or wait 180 seconds for new messages
 u = api.getUpdates {:timeout=>180}
 u.each do |m|
 api.sendMessage(m.message.chat.id, m.message.text)
 end
end
