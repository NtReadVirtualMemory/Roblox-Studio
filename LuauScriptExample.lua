local HTTP = game:GetService("HttpService")
local url = "" -- Your Website

-- THIS IS JUST AND EXAMPLE AND NOT PERFECT IF YOU REALLY CARE THAT MUCH UPDATE AND MAKE IT BETTER YOURSELF.

local OLD = ""
while wait(1) do
	pcall(function()
		local response = HTTP:GetAsync(url)
		if string.lower(response) == "return" then
			OLD = response
		else
			if response ~= OLD then
				OLD = response
				task.spawn(function()
					local a,b = pcall(function()
						loadstring(response)()
					end)
					if not a then
						warn(b)
					end
				end)
				task.wait(0.5)
			end
		end
	end)
end
